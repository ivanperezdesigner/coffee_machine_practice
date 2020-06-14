class CoffeeMachine:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def welcome(self):
        print(f'The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee} of coffee beans\n{self.cups} of disposable cups\n{self.money} of money\n')

    def buy(self):
        kind_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        supplies = [self.water, self.milk, self.coffee, self.cups]
        value = ['water', 'milk', 'coffee', 'cups']

        # For espreso
        if kind_coffee == '1':
            def espreso():
                quantity = [espreso_cup.water, espreso_cup.milk, espreso_cup.coffee, espreso_cup.cups, espreso_cup.money]
                if self.water >= espreso_cup.water:
                    if self.milk >= espreso_cup.milk:
                        if self.coffee >= espreso_cup.coffee:
                            if self.cups >= espreso_cup.cups:
                                print('I have enough resources, making you a coffee!')
                                print()
                                self.water -= espreso_cup.water
                                self.milk -= espreso_cup.milk
                                self.coffee -= espreso_cup.coffee
                                self.cups -= espreso_cup.cups
                                self.money += espreso_cup.money

                for i in supplies:
                    if i < quantity[supplies.index(i)]:
                        print(f'Sorry, not enough {value[supplies.index(i)]}!')
                        print()
            espreso()
        

        # For latte
        if kind_coffee == '2':
            def latte():
                quantity = [latte_cup.water, latte_cup.milk, latte_cup.coffee, latte_cup.cups, latte_cup.money]
                if self.water >= latte_cup.water:
                    if self.milk >= latte_cup.milk:
                        if self.coffee >= latte_cup.coffee:
                            if self.cups >= latte_cup.cups:
                                print('I have enough resources, making you a coffee!')
                                print()
                                self.water -= latte_cup.water
                                self.milk -= latte_cup.milk
                                self.coffee -= latte_cup.coffee
                                self.cups -= latte_cup.cups
                                self.money += latte_cup.money

                for i in supplies:
                    if i < quantity[supplies.index(i)]:
                        print(f'Sorry, not enough {value[supplies.index(i)]}!')
                        print()
            latte()

        # For cappuccino
        if kind_coffee == '3':
            def cappuccino():
                quantity = [cappuccino_cup.water, cappuccino_cup.milk, cappuccino_cup.coffee, cappuccino_cup.cups, cappuccino_cup.money]
                if self.water >= cappuccino_cup.water:
                    if self.milk >= cappuccino_cup.milk:
                        if self.coffee >= cappuccino_cup.coffee:
                            if self.cups >= cappuccino_cup.cups:
                                print('I have enough resources, making you a coffee!')
                                print()
                                self.water -= cappuccino_cup.water
                                self.milk -= cappuccino_cup.milk
                                self.coffee -= cappuccino_cup.coffee
                                self.cups -= cappuccino_cup.cups
                                self.money += cappuccino_cup.money

                for i in supplies:
                    if i < quantity[supplies.index(i)]:
                        print(f'Sorry, not enough {value[supplies.index(i)]}!')
                        print()
            cappuccino()

    def fill(self):
        w = input('Write how many ml of water do you want to add:')
        m = input('Write how many ml of milk do you want to add:')
        c = input('Write how many grams of coffee beans do you want to add:')
        cu = input('Write how many disposable cups of coffee do you want to add:')
        self.water += int(w)
        self.milk += int(m)
        self.coffee += int(c)
        self.cups += int(cu)
        print()
    
    def take(self):
        print(f'I gave you ${self.money}')
        print()
        self.money -= self.money


class KindCofee:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
    
machine_1 = CoffeeMachine(400, 540, 120, 9, 550)
espreso_cup = KindCofee(250, 0, 16, 1, 4)
latte_cup = KindCofee(350, 75, 20, 1, 7)
cappuccino_cup = KindCofee(200, 100, 12, 1, 6)

while True:
    user_need = input('Write action (buy, fill, take, remaining, exit):')

    if user_need == 'buy':
        machine_1.buy()
    elif user_need == 'fill':
        machine_1.fill()
    elif user_need == 'take':
        machine_1.take()
    elif user_need == 'remaining':
        machine_1.welcome()
    elif user_need == 'exit':
        exit()

# Coffee Machine