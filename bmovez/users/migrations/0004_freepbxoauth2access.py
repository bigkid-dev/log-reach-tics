# Generated by Django 4.0.10 on 2023-05-07 14:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_resetpasswordotp_datetime_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreePBXOauth2Access',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('token_type', models.CharField(max_length=100)),
                ('expires_in', models.DateTimeField()),
                ('expired', models.BooleanField(default=False)),
                ('signed_access_token', models.TextField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
