# Generated by Django 2.2.6 on 2021-10-19 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommandGroupModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='命令分组名称')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '命令分组',
                'verbose_name_plural': '命令分组',
                'db_table': 'command_group',
            },
        ),
        migrations.CreateModel(
            name='CommandLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('command', models.CharField(max_length=255, verbose_name='指令')),
                ('block_type', models.CharField(max_length=8, null=True, verbose_name='阻断类型')),
                ('intercept_command', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('y', '执行'), ('n', '未执行')], default='n', max_length=8, verbose_name='指令是否执行')),
                ('hostname', models.CharField(max_length=255, verbose_name='服务器IP')),
                ('user', models.CharField(max_length=32, null=True, verbose_name='用户名')),
                ('opt_user', models.CharField(max_length=32, null=True, verbose_name='操作用户')),
            ],
            options={
                'verbose_name': '命令日志',
                'verbose_name_plural': '命令日志',
                'db_table': 'command_log',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CommandModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('command', models.CharField(max_length=255, verbose_name='命令名称')),
                ('block_type', models.IntegerField(default=1, verbose_name='阻断类型')),
                ('block_info', models.CharField(max_length=255, verbose_name='阻断提示信息')),
            ],
            options={
                'verbose_name': '命令',
                'verbose_name_plural': '命令',
                'db_table': 'command',
            },
        ),
        migrations.CreateModel(
            name='CredentialGroupModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='分组名称')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '凭据分组',
                'verbose_name_plural': '凭据分组',
                'db_table': 'credential_group',
            },
        ),
        migrations.CreateModel(
            name='CredentialModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='凭据名称')),
                ('login_type', models.CharField(choices=[('auto', '自动登录'), ('hand', '手动登录')], default='auto', max_length=20, verbose_name='登录方式')),
                ('credential_type', models.CharField(choices=[('password', '密码凭据'), ('ssh_key', 'SSH秘钥')], default='password', max_length=20, verbose_name='凭据类型')),
                ('login_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='资源账户')),
                ('login_password', models.CharField(blank=True, max_length=500, null=True, verbose_name='密码')),
                ('ssh_key', models.TextField(blank=True, null=True, verbose_name='SSH Key')),
                ('passphrase', models.CharField(blank=True, max_length=500, null=True, verbose_name='通行码')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='描述')),
                ('credential_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bastion.CredentialGroupModel', verbose_name='凭据分组')),
            ],
            options={
                'verbose_name': '凭据',
                'verbose_name_plural': '凭据',
                'db_table': 'credential',
            },
        ),
        migrations.CreateModel(
            name='HostCredentialRelationshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('credential', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credential_host', to='bastion.CredentialModel')),
                ('credential_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credential_group_host', to='bastion.CredentialGroupModel')),
            ],
            options={
                'verbose_name': '主机与凭据，凭据组关联',
                'verbose_name_plural': '主机与凭据，凭据组关联',
                'db_table': 'host_credential_relationship',
            },
        ),
        migrations.CreateModel(
            name='HostGroupModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='主机分组名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_group', to='bastion.HostGroupModel', verbose_name='上级')),
            ],
            options={
                'verbose_name': '主机分组',
                'verbose_name_plural': '主机分组',
                'db_table': 'host_group',
            },
        ),
        migrations.CreateModel(
            name='HostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('host_name_code', models.CharField(default='', max_length=200, verbose_name='主机唯一标识')),
                ('host_name', models.CharField(max_length=100, verbose_name='主机名称')),
                ('system_type', models.CharField(choices=[('Linux', 'Linux'), ('Windows', 'Windows')], default='Linux', max_length=20, verbose_name='系统类型')),
                ('protocol_type', models.CharField(choices=[('SSH', 'SSH'), ('RDP', 'RDP'), ('Telnet', 'Telnet'), ('VNC', 'VNC')], default='SSH', max_length=20, verbose_name='协议类型')),
                ('host_address', models.CharField(max_length=150, verbose_name='主机地址')),
                ('resource_from', models.CharField(blank=True, default='hand', max_length=30, null=True, verbose_name='数据来源')),
                ('port', models.IntegerField(default=22, verbose_name='端口')),
                ('description', models.CharField(blank=True, max_length=3000, null=True, verbose_name='主机描述')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_group', to='bastion.HostGroupModel', verbose_name='所属分组')),
            ],
            options={
                'verbose_name': '主机资源',
                'verbose_name_plural': '主机资源',
                'db_table': 'host',
            },
        ),
        migrations.CreateModel(
            name='OperationLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=100, verbose_name='操作人用户名')),
                ('operation_type', models.CharField(max_length=50, verbose_name='操作类型')),
                ('operation_object', models.CharField(max_length=100, verbose_name='操作对象')),
                ('operation_content', models.CharField(max_length=5000, verbose_name='操作内容')),
                ('parameter', models.TextField(blank=True, null=True, verbose_name='参数')),
                ('method', models.CharField(blank=True, max_length=20, null=True, verbose_name='请求方式')),
            ],
            options={
                'verbose_name': '操作日志',
                'verbose_name_plural': '操作日志',
                'db_table': 'operation_log',
            },
        ),
        migrations.CreateModel(
            name='StrategyAccessModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='策略名称')),
                ('start_time', models.DateTimeField(null=True, verbose_name='生效时间')),
                ('end_time', models.DateTimeField(null=True, verbose_name='失效时间')),
                ('file_upload', models.BooleanField(default=False, verbose_name='文件上传')),
                ('file_download', models.BooleanField(default=False, verbose_name='文件下载')),
                ('file_manager', models.BooleanField(default=False, verbose_name='文件管理')),
                ('copy_tool', models.BooleanField(default=False, verbose_name='剪切板')),
                ('login_time_limit', models.TextField(blank=True, null=True, verbose_name='登录时段限制')),
                ('ip_limit', models.IntegerField(default=1)),
                ('limit_list', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '访问策略',
                'verbose_name_plural': '访问策略',
                'db_table': 'strategy_access',
            },
        ),
        migrations.CreateModel(
            name='StrategyCommandModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='命令策略名称')),
                ('start_time', models.DateTimeField(null=True, verbose_name='生效时间')),
                ('end_time', models.DateTimeField(null=True, verbose_name='失效时间')),
                ('login_time_limit', models.TextField(blank=True, verbose_name='登录时段限制')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '命令策略',
                'verbose_name_plural': '命令策略',
                'db_table': 'strategy_command',
            },
        ),
        migrations.CreateModel(
            name='UserGroupModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, verbose_name='用户组名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '用户组',
                'verbose_name_plural': '用户组',
                'db_table': 'user_group',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=30, null=True, verbose_name='手机号')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='邮箱')),
                ('ch_name', models.CharField(max_length=50, null=True, verbose_name='中文名')),
                ('role', models.IntegerField(verbose_name='用户角色')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user_info',
            },
        ),
        migrations.CreateModel(
            name='UserGroupRelationshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to='bastion.UserInfo', verbose_name='用户')),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_user', to='bastion.UserGroupModel', verbose_name='组')),
            ],
            options={
                'verbose_name': '用户、组关联表',
                'verbose_name_plural': '用户、组关联表',
                'db_table': 'group_user_relationship',
            },
        ),
        migrations.CreateModel(
            name='StrategyCommandUserGroupRelationshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('strategy_command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategy_command_user_or_user_group', to='bastion.StrategyCommandModel', verbose_name='关联策略')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_strategy_command', to='bastion.UserInfo', verbose_name='用户')),
                ('user_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_group_strategy_command', to='bastion.UserGroupModel', verbose_name='用户组')),
            ],
            options={
                'verbose_name': '命令策略关联用户，用户组',
                'verbose_name_plural': '命令策略关联用户，用户组',
                'db_table': 'strategy_command_user_group_relationship',
            },
        ),
        migrations.AddField(
            model_name='strategycommandmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bastion.UserInfo', verbose_name='创建人'),
        ),
        migrations.CreateModel(
            name='StrategyCommandGroupRelationshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('command', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='command_strategy', to='bastion.CommandModel', verbose_name='命令')),
                ('command_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='command_group_strategy', to='bastion.CommandGroupModel', verbose_name='命令分组')),
                ('strategy_command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategy_command_or_group', to='bastion.StrategyCommandModel', verbose_name='命令策略')),
            ],
            options={
                'verbose_name': '命令策略关联命令，命令分组',
                'verbose_name_plural': '命令策略关联命令，命令分组',
                'db_table': 'strategy_command_group_relationship',
            },
        ),
        migrations.CreateModel(
            name='StrategyCommandCredentialHostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('credential_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_credential_group_strategy_command', to='bastion.CredentialGroupModel', verbose_name='关联凭证分组')),
                ('credential_host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_credential_strategy_command', to='bastion.HostCredentialRelationshipModel')),
                ('strategy_command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_strategy_command_credential_or_credential_group', to='bastion.StrategyCommandModel', verbose_name='关联策略')),
            ],
            options={
                'ordering': ['-create_time', '-update_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StrategyAccessUserGroupRelationshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('strategy_access', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategy_access_user_or_user_group', to='bastion.StrategyAccessModel', verbose_name='关联策略')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_strategy_access', to='bastion.UserInfo', verbose_name='关联用户')),
                ('user_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_group_strategy_access', to='bastion.UserGroupModel', verbose_name='关联用户组')),
            ],
            options={
                'verbose_name': '访问策略关联用户，用户组',
                'verbose_name_plural': '访问策略关联用户，用户组',
                'db_table': 'strategy_access_user_group_relationship',
            },
        ),
        migrations.AddField(
            model_name='strategyaccessmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bastion.UserInfo', verbose_name='创建人'),
        ),
        migrations.CreateModel(
            name='StrategyAccessCredentialHostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('credential_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_credential_group_strategy_access', to='bastion.CredentialGroupModel', verbose_name='关联凭证分组')),
                ('credential_host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_credential_host_strategy_access', to='bastion.HostCredentialRelationshipModel')),
                ('strategy_access', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_strategy_access_credential_or_credential_group', to='bastion.StrategyAccessModel', verbose_name='关联策略')),
            ],
            options={
                'ordering': ['-create_time', '-update_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SessionLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_time', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='结束时间')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('channel', models.CharField(editable=False, max_length=100, unique=True, verbose_name='通道名')),
                ('log_name', models.CharField(editable=False, max_length=100, verbose_name='日志名')),
                ('host_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='主机名称')),
                ('system_type', models.CharField(default='Linux', max_length=100, verbose_name='系统类型')),
                ('host_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='主机地址')),
                ('port', models.IntegerField(default=22, verbose_name='端口')),
                ('protocol_type', models.CharField(blank=True, max_length=20, null=True, verbose_name='协议类型')),
                ('login_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='系统用户')),
                ('login_type', models.IntegerField(default=1)),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='开始时间')),
                ('is_finished', models.BooleanField(default=False, verbose_name='是否完成')),
                ('user', models.CharField(max_length=100, verbose_name='用户名')),
                ('width', models.PositiveIntegerField(default=1024, verbose_name='宽度')),
                ('height', models.PositiveIntegerField(default=768, verbose_name='高度')),
                ('guacamole_client_id', models.CharField(blank=True, editable=False, max_length=100, verbose_name='Gucamole通道名称')),
                ('tag', models.CharField(blank=True, max_length=100, null=True, verbose_name='标签')),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bastion.HostModel', verbose_name='主机')),
            ],
            options={
                'verbose_name': '会话日志',
                'verbose_name_plural': '会话日志',
                'db_table': 'session_log',
                'ordering': ['-start_time'],
            },
        ),
        migrations.CreateModel(
            name='SessionCommandHistoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('command', models.TextField()),
                ('session_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bastion.SessionLogModel')),
            ],
            options={
                'db_table': 'session_command_history',
            },
        ),
        migrations.AddField(
            model_name='hostmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bastion.UserInfo', verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='hostgroupmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bastion.UserInfo', verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='hostcredentialrelationshipmodel',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_credential_or_credential_group', to='bastion.HostModel'),
        ),
        migrations.AddField(
            model_name='hostcredentialrelationshipmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bastion.UserInfo', verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='credentialmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bastion.UserInfo', verbose_name='创建人'),
        ),
        migrations.CreateModel(
            name='CredentialGroupStrategyCommandRelationshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('credential', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credential_strategy_command', to='bastion.CredentialModel', verbose_name='关联凭证')),
                ('credential_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credential_group_strategy_command', to='bastion.CredentialGroupModel', verbose_name='关联凭证分组')),
                ('strategy_command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategy_command_credential_or_credential_group', to='bastion.StrategyCommandModel', verbose_name='关联策略')),
            ],
            options={
                'verbose_name': '凭据凭据分组关联命令策略',
                'verbose_name_plural': '凭据凭据分组关联命令策略',
                'db_table': 'credential_Group_strategy_command_relationship',
            },
        ),
        migrations.CreateModel(
            name='CredentialGroupStrategyAccessRelationshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('credential', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credential_strategy_access', to='bastion.CredentialModel', verbose_name='关联凭证')),
                ('credential_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credential_group_strategy_access', to='bastion.CredentialGroupModel', verbose_name='关联凭证分组')),
                ('strategy_access', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategy_access_credential_or_credential_group', to='bastion.StrategyAccessModel', verbose_name='关联策略')),
            ],
            options={
                'verbose_name': '凭据凭据分组关联访问策略',
                'verbose_name_plural': '凭据凭据分组关联访问策略',
                'db_table': 'credential_Group_strategy_access_relationship',
            },
        ),
        migrations.AddField(
            model_name='credentialgroupmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bastion.UserInfo', verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='commandmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bastion.UserInfo', verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='commandgroupmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bastion.UserInfo', verbose_name='创建人'),
        ),
        migrations.AlterUniqueTogether(
            name='hostcredentialrelationshipmodel',
            unique_together={('host', 'credential', 'credential_group')},
        ),
        migrations.CreateModel(
            name='CredentialGroupRelationshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('credential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credential_queryset', to='bastion.CredentialModel', verbose_name='关联凭据')),
                ('credential_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credential_group_queryset', to='bastion.CredentialGroupModel', verbose_name='关联凭据分组')),
            ],
            options={
                'verbose_name': '凭据，凭据分组关联表',
                'verbose_name_plural': '凭据，凭据分组关联表',
                'db_table': 'credential_group_relationship',
                'unique_together': {('credential', 'credential_group')},
            },
        ),
        migrations.CreateModel(
            name='CommandGroupRelationshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='command_queryset', to='bastion.CommandModel', verbose_name='命令')),
                ('command_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='command_group_queryset', to='bastion.CommandGroupModel', verbose_name='命令分组')),
            ],
            options={
                'verbose_name': '命令分组关联',
                'verbose_name_plural': '命令分组关联',
                'db_table': 'command_group_relationship',
                'unique_together': {('command', 'command_group')},
            },
        ),
    ]