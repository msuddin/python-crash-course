import pizza
import greeter as g
from formatted_name import get_full_name

pizza.make_pizza(5, 'cheese')
person = get_full_name('jami', 'south')
print(person)
g.greet_user_by_name('jami')