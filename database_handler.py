from sqlalchemy import create_engine, Column, Integer, String, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DataAccess:
    def __init__(self):
        self.engine = None
        self.conn_string = 'sqlite:///contact_book.db'

    def connect(self):
        self.engine = create_engine(self.conn_string, echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def fetch_data_all(self):
        session = self.Session()
        result = session.query(Contact).all()
        return result

    def fetch_filtered_data(self, request_type, criteria):
        session = self.Session()
        my_result = []
        if request_type=='group':
            for c in criteria:
                my_result.append(session.query(Contact).
                                 filter(Contact.group==c))
        else:
            for c in criteria:
                c = c.title()
                my_result.append(session.query(Contact).
                                 filter(Contact.surname == c))
        return my_result

    def add_data(self, data_list):
        session = self.Session()
        new = Contact(name=data_list[0], surname=data_list[1],
                      phone=data_list[2], email=data_list[3],
                      birthday=data_list[4], group=data_list[5])
        session.add(new)
        session.commit()

    def edit_data(self, old_surname, data_list):
        session = self.Session()
        update = session.query(Contact).filter(Contact.surname == old_surname).one()
        update.name = data_list[0]
        update.surname = data_list[1]
        update.phone = data_list[2]
        update.email = data_list[3]
        update.birthday = data_list[4]
        update.group = data_list[5]
        session.commit()

    def del_data(self, data_list):
        session = self.Session()
        old = session.query(Contact).filter(and_(Contact.name == data_list[0],
                                            Contact.surname == data_list[1]))
        for record in old:
            session.delete(record)
        session.commit()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(Integer, unique=True)
    email = Column(String, unique=True)
    birthday = Column(String)
    group = Column(String)

if __name__=="__main__":
    print("This is database handler module.")