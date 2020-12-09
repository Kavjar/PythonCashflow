from migrate import db

Base = db.Model

class Account(Base):
    __tablename__ = "account"
    idaccount = db.Column(db.INTEGER, primary_key=True)
    sum = db.Column(db.INTEGER, nullable=True)

class Expenses(Base):
    __tablename__ = "expenses"
    idexpenses = db.Column(db.INTEGER, primary_key=True)
    item = db.Column(db.VARCHAR(45))
    price = db.Column(db.INTEGER)
    date = db.Column(db.DATETIME(10))
    account_id = db.Column(db.INTEGER, db.ForeignKey(Account.idaccount))
    Account= db.relationship(Account)

class Incomes(Base):
    __tablename__ = "incomes"
    idincomes = db.Column(db.INTEGER, primary_key=True)
    incomeName = db.Column(db.VARCHAR(45), nullable=False)
    sum = db.Column(db.INTEGER)
    date = db.Column(db.DATETIME(10))
    account_id = db.Column(db.INTEGER, db.ForeignKey(Account.idaccount))
    Account = db.relationship(Account)

class Family(Base):
    __tablename__ = "family"
    idfamily = db.Column(db.INTEGER, primary_key=True)
    surname = db.Column(db.VARCHAR(45), nullable=False)
    budget = db.Column(db.INTEGER)
    account_id = db.Column(db.INTEGER, db.ForeignKey(Account.idaccount))
    Account = db.relationship(Account)


class User(Base):
    __tablename__ = "user"
    iduser = db.Column(db.INTEGER, primary_key=True)
    username= db.Column(db.VARCHAR(45), nullable=True)
    firstname = db.Column(db.VARCHAR(45))
    lastname = db.Column(db.VARCHAR(45))
    email = db.Column(db.VARCHAR(45))
    password = db.Column(db.VARCHAR(45), nullable=True)
    phone = db.Column(db.VARCHAR(45))
    account_id = db.Column(db.INTEGER, db.ForeignKey(Account.idaccount))
    Account = db.relationship(Account)
    family_id = db.Column(db.INTEGER, db.ForeignKey(Family.idfamily), nullable=True)
    Family = db.relationship(Family)

class Transaction(Base):
    __tablename__ = "transactiondata"
    idtransaction = db.Column(db.INTEGER, primary_key=True)
    money = db.Column(db.INTEGER, nullable=True)
    direction = db.Column(db.INTEGER, nullable=True)
    family_id = db.Column(db.INTEGER, db.ForeignKey(Family.idfamily))
    Family = db.relationship(Family)
    account_id = db.Column(db.INTEGER, db.ForeignKey(Account.idaccount))
    Account = db.relationship(Account)


db.create_all()