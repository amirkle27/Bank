import pytest
import Bank
from datetime import datetime
from Bank import bank_accounts, sample_account, account_by_number, account_by_id, account_by_name, sorted_by_balance, today_transactions

#@pytest.fixture

def test_printing_account_1001 (monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"1001")
    account_number = 1001
    account = bank_accounts[account_number]
    expected_keys = {"first_name","last_name","id_number","balance","transactions_to_execute","transaction_history"}
    expected_values = {
        "first_name": "Alice",
        "last_name": "Smith",
        "id_number": "123456789",
        "balance": 2500.50,
        "transactions_to_execute": [
            ("2024-08-26 14:00:00", 1001, 1002, 300), ("2024-08-26 15:00:00", 1001, 1003, 200), ("2024-08-26 10:00:00", 1001, 1003, 200)],
        "transaction_history": [
            ("2024-08-15 09:00:00", 1001, 1002, 500, "2024-08-15 09:30:00", 1001, 1002, 1000)]
    }

    assert set(account.keys()) == expected_keys
    for key,value in expected_values.items():
        assert account[key] == value

def test_printing_account_1002 (monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"1002")
    account_number = 1002
    account = bank_accounts[account_number]
    expected_keys = {"first_name","last_name","id_number","balance","transactions_to_execute","transaction_history"}
    expected_values = {
        "first_name": "Bob",
        "last_name": "Johnson",
        "id_number": "987654321",
        "balance": -3900.75,
        "transactions_to_execute": [("2025-01-23 10:05:00", 1002, 1001, 3000), ("2025-08-17 15:00:00", 1002, 1003, 2000)],
        "transaction_history": [("2024-08-25 09:00:00", 1002, 1004, 500, "2024-08-15 09:30:00", 1002, 1004, 1000)]
    }

    assert set(account.keys()) == expected_keys
    for key,value in expected_values.items():
        assert account[key] == value

def test_printing_account_1003 (monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"1003")
    account_number = 1003
    account = bank_accounts[account_number]
    expected_keys = {"first_name","last_name","id_number","balance","transactions_to_execute","transaction_history"}
    expected_values = {
        "first_name": "Charles",
        "last_name": "Bronson",
        "id_number": "222014651",
        "balance": -40000000.4,
        "transactions_to_execute": [("2024-09-06 10:05:00", 1003, 1001, 30000), ("2025-02-23 15:00:00", 1003, 1004, 400)],
        "transaction_history": [("2022-01-23 10:05:00", 1003, 1001, 30000), ("2022-02-23 15:00:00", 1003, 1002, 400)]
    }

    assert set(account.keys()) == expected_keys
    for key,value in expected_values.items():
        assert account[key] == value

def test_printing_account_1004 (monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"1004")
    account_number = 1004
    account = bank_accounts[account_number]
    expected_keys = {"first_name","last_name","id_number","balance","transactions_to_execute","transaction_history"}
    expected_values = {
        "first_name": "Arnon",
        "last_name": "Zadok",
        "id_number": "323395176",
        "balance": -50000,
        "transactions_to_execute": [("2025-07-11 12:00:00", 1004, 1001, 30), ("2025-09-15 10:00:00", 1004, 1003, 15)],
        "transaction_history": [("2024-08-25 14:00:00", 1004, 1002, 1500), ("2001-01-28 12:07:00", 1004, 1002, 9200)]
        }

    assert set(account.keys()) == expected_keys
    for key,value in expected_values.items():
        assert account[key] == value

def test_id_1001 ():
    account_number = 1001
    account = bank_accounts[account_number]
    id = "123456789"
    assert id == account['id_number']

def test_today ():
    account_number = 1003
    account = bank_accounts[account_number]
    today = datetime.today().date()

    assert any(datetime.strptime(txn[0], "%Y-%m-%d %H:%M:%S").date() == today for txn in account['transactions_to_execute'])









