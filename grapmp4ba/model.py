# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import MYSQL_CONF as conf

Base = declarative_base()
metadata = Base.metadata


class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    date_id = Column(Integer)
    title = Column(String(255))
    link = Column(String(255))
    definition = Column(Integer)
    pic_path = Column(String(255))
    dl_link = Column(String(255))
    detail = Column(String)
    hashcode = Column(String(255))


# 初始化数据库连接:
engine = create_engine('mysql+mysqldb://%s:%s@%s:%s/%s' % (conf['username'], '', conf['host'],conf['port'],conf['database']))
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# session = DBSession()
# a = Movie(date_id=20160126, title='test', link='http', definition=1080, pic_path='/opt/pic', dl_link='https://', detail='test', hashcode='fsetetesfgaf43t23rg')
# session.add(a)
# session.commit()
# session.close()