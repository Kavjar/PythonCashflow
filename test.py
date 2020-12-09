from models import *

db.create_all()
account=Account(idaccount=2,sum=3)
expenses=Expenses(item="jojo",Account=account)
incomes=Incomes(incomeName="Loli",Account=account)
family=Family(idfamily=4,surname="browni(hochy)",Account=account)
user=User(iduser=5,Account=account,Family=family)
transaction= Transaction(idtransaction=2,Account=account,Family=family)
db.session.add(account)
db.session.add(expenses)
db.session.add(incomes)
db.session.add(family)
db.session.add(user)
db.session.add(transaction)

db.session.commit()