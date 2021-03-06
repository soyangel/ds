from __future__ import absolute_import

from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from ds.config import db
from ds.db.types.json import JSONEncodedDict


class App(db.Model):
    __tablename__ = 'app'

    id = Column(Integer, primary_key=True)
    repository_id = Column(Integer,
                           ForeignKey('repository.id', ondelete="CASCADE"),
                           nullable=False)
    name = Column(String(200), nullable=False, unique=True)
    provider = Column(String(64))
    data = Column(JSONEncodedDict)
    date_created = Column(DateTime, default=datetime.utcnow, nullable=False)

    @property
    def provider_config(self):
        return self.data['provider_config']
