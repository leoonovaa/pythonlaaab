import pytest
from Bank import BankAccount

# Тест на створення рахунку з початковим балансом
def test_create_account_with_initial_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100

# Тест на депозит коштів та перевірку балансу
def test_deposit_funds_and_check_balance():
    account = BankAccount(100)
    account.deposit(50)
    assert account.get_balance() == 150

# Тест на зняття коштів та перевірку балансу
def test_withdraw_funds_and_check_balance():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50

# Тест на спробу зняття більшої суми, ніж доступно
def test_withdraw_more_than_balance():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Insufficient funds."):
        account.withdraw(150)

# Тест на спробу внести негативну суму
def test_deposit_negative_amount():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account.deposit(-50)

# Тест на спробу зняття негативної суми
def test_withdraw_negative_amount():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive."):
        account.withdraw(-50)

# Тест на спробу створення рахунку з негативним початковим балансом
def test_create_account_with_negative_balance():
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount(-100)
