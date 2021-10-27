from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name = 'chat',
            fields = [
                ('chat_id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_group_chat', models.NullBooleanField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to = 'learn.user', related_name='id'))
            ]
        ),

        migrations.CreateModel(
            name = 'user_chat',
            fields = [
                ('user_chat_id', models.UUIDField(primary_key=True, serialize=False)),
                ("chat_id", models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, to = 'learn.Chat', related_name='chat_id')),
                ('user_id', models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, to = 'learn.user', related_name='id'))
            ]
        )
    ]