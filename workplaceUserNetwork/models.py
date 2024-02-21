from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, default="")
    note = models.TextField(default="")

    def __str__(self):
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=100, default="")
    note = models.TextField(default="")

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username

class Interaction(models.Model):
    name = models.CharField(max_length=100, default="")
    note = models.TextField(default="")

    def __str__(self):
        return self.name

class WorkplaceUserNetwork(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user_networks', default=None)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user_networks', default=None)
    posting_division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='posting_divisions', default=None)
    comment_division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='comment_divisions', default=None)
    posting_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='posting_departments', default=None)
    comment_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='comment_departments', default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type_of_interaction = models.ForeignKey(Interaction, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"WorkplaceUserNetwork {self.pk}"