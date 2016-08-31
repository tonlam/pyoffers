# coding: utf-8
from .core import Model, ModelManager


class Goal(Model):
    """
    A Goal for an Offer.
    """

    def update(self, **kwargs):
        return self._manager.update(self['id'], **kwargs)


class GoalManager(ModelManager):
    model = Goal
    name = 'goals'

    def create(self, **kwargs):
        return self._call('create', data=kwargs)

    def update(self, id, **kwargs):
        return self._call('update', id=id, data=kwargs)

    def find_by_id(self, id):
        return self._call('findById', id=id)

    def find_all(self, sort=None, limit=None, page=None, contain=None, **kwargs):
        return self._call(
            'findAll', filters=kwargs, sort=sort, limit=limit, page=page, contain=contain, single_result=False
        )
