from django.db import models

class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    brgy = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    birthdate = models.DateField()

class Account(models.Model):
    ACCOUNT_TYPE = (
        ('savings', 'Savings'),
        ('checking', 'Checking'),
    )
    account_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="accounts")
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.account_number} ({self.user.username})"

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('payment', 'Payment'),
    )

    STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"

class Transfer(models.Model):
    TRANSFER_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    transfer_id = models.AutoField(primary_key=True)
    sender_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="sent_transfers")
    receiver_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="received_transfers")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50, choices=TRANSFER_STATUS)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transfer {self.amount} from {self.sender_account} to {self.receiver_account}"

class Bill(models.Model):
    BILL_STATUS = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    )
    bill_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="bills")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=50, choices=BILL_STATUS)

    def __str__(self):
        return f"{self.bill_type} - {self.amount} ({self.status})"
