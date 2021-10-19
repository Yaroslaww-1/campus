from django.db import migrations, models
import django.db.models.deletion
from django.utils import timezone

class Migration(migrations.Migration):
    dependencies = [
        ('learn', '0003_add_content_and_user_reference_to_post'),
    ]

    operations = [
        migrations.CreateModel(
            name = 'Message',
            fields = [
                ('message_id', models.UUIDField(primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, to = 'learn.post', related_name='created_by')),
                ('created_on', models.DateTimeField(default=timezone.now)),
                ('content', models.TextField(null=False))
            ]
        )
    ]

