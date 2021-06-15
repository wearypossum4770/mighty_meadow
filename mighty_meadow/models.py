from django.db.models import BooleanField, DateTimeField, Manager, Model, query
from django.utils import timezone


class SoftDeleteQuerySet(query.QuerySet):
    def delete(self):
        return self.update(is_deleted=True, deleted_at=timezone.now())

    def hard_delete(self):
        return super().delete()


class SoftDeleteManager(Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, self._db).filter(is_deleted=False)


class DeletedQuerySet(query.QuerySet):
    def restore(self, *args, **kwargs):
        qs = self.filter(*args, **kwargs)
        qs.update(is_deleted=False)


class DeletedManager(Manager):
    def get_queryset(self):
        return DeletedQuerySet(self.model, self._db).filter(is_deleted=True)


class SoftDeleteModel(Model):
    is_deleted = BooleanField(default=False)
    deleted_at = DateTimeField(blank=True, null=True)

    objects = SoftDeleteManager()
    deleted_objects = DeletedManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
