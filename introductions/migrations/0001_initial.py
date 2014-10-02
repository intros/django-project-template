# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'introductions_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('preferred_email_address', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'introductions', ['Person'])

        # Adding model 'PersonEmail'
        db.create_table(u'introductions_personemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['introductions.Person'], null=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('extracted_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'introductions', ['PersonEmail'])

        # Adding model 'PersonComment'
        db.create_table(u'introductions_personcomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['introductions.Person'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('parent_comment', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_comment_set', null=True, to=orm['introductions.PersonComment'])),
        ))
        db.send_create_signal(u'introductions', ['PersonComment'])

        # Adding model 'TaggedIntroduction'
        db.create_table(u'introductions_taggedintroduction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'introductions_taggedintroduction_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['introductions.Introduction'])),
        ))
        db.send_create_signal(u'introductions', ['TaggedIntroduction'])

        # Adding model 'Introduction'
        db.create_table(u'introductions_introduction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_alias', self.gf('django.db.models.fields.SlugField')(default=u'ejrPFqVC', unique=True, max_length=16)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['introductions.Person'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('from_addr', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('delivered_to', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('to_addrs', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cc_addrs', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('introduction_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('mailbox_message', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['django_mailbox.Message'], unique=True, null=True)),
        ))
        db.send_create_signal(u'introductions', ['Introduction'])

        # Adding M2M table for field introducees on 'Introduction'
        m2m_table_name = db.shorten_name(u'introductions_introduction_introducees')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('introduction', models.ForeignKey(orm[u'introductions.introduction'], null=False)),
            ('personemail', models.ForeignKey(orm[u'introductions.personemail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['introduction_id', 'personemail_id'])

        # Adding model 'IntroductionEmail'
        db.create_table(u'introductions_introductionemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('introduction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['introductions.Introduction'])),
            ('email', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_mailbox.Message'])),
        ))
        db.send_create_signal(u'introductions', ['IntroductionEmail'])

        # Adding model 'IntroductionComment'
        db.create_table(u'introductions_introductioncomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['introductions.Person'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('introduction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['introductions.Introduction'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('parent_comment', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_comment_set', null=True, to=orm['introductions.IntroductionComment'])),
        ))
        db.send_create_signal(u'introductions', ['IntroductionComment'])

        # Adding model 'IntroductionReminder'
        db.create_table(u'introductions_introductionreminder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['introductions.Person'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('introduction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['introductions.Introduction'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('parent_reminder', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_reminder_set', null=True, to=orm['introductions.IntroductionReminder'])),
            ('requested', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('ignore', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'introductions', ['IntroductionReminder'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'introductions_person')

        # Deleting model 'PersonEmail'
        db.delete_table(u'introductions_personemail')

        # Deleting model 'PersonComment'
        db.delete_table(u'introductions_personcomment')

        # Deleting model 'TaggedIntroduction'
        db.delete_table(u'introductions_taggedintroduction')

        # Deleting model 'Introduction'
        db.delete_table(u'introductions_introduction')

        # Removing M2M table for field introducees on 'Introduction'
        db.delete_table(db.shorten_name(u'introductions_introduction_introducees'))

        # Deleting model 'IntroductionEmail'
        db.delete_table(u'introductions_introductionemail')

        # Deleting model 'IntroductionComment'
        db.delete_table(u'introductions_introductioncomment')

        # Deleting model 'IntroductionReminder'
        db.delete_table(u'introductions_introductionreminder')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'django_mailbox.mailbox': {
            'Meta': {'object_name': 'Mailbox'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'from_email': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'django_mailbox.message': {
            'Meta': {'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'encoded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'from_header': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_reply_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'replies'", 'null': 'True', 'to': u"orm['django_mailbox.Message']"}),
            'mailbox': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': u"orm['django_mailbox.Mailbox']"}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'outgoing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'processed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'read': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to_header': ('django.db.models.fields.TextField', [], {})
        },
        u'introductions.introduction': {
            'Meta': {'object_name': 'Introduction'},
            'cc_addrs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delivered_to': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email_alias': ('django.db.models.fields.SlugField', [], {'default': "u'AjovAWyx'", 'unique': 'True', 'max_length': '16'}),
            'from_addr': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introducees': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['introductions.PersonEmail']", 'symmetrical': 'False'}),
            'introduction_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'mailbox_message': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['django_mailbox.Message']", 'unique': 'True', 'null': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['introductions.Person']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'to_addrs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'introductions.introductioncomment': {
            'Meta': {'object_name': 'IntroductionComment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['introductions.Introduction']"}),
            'parent_comment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_comment_set'", 'null': 'True', 'to': u"orm['introductions.IntroductionComment']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['introductions.Person']"})
        },
        u'introductions.introductionemail': {
            'Meta': {'object_name': 'IntroductionEmail'},
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_mailbox.Message']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['introductions.Introduction']"})
        },
        u'introductions.introductionreminder': {
            'Meta': {'object_name': 'IntroductionReminder'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignore': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'introduction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['introductions.Introduction']"}),
            'parent_reminder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_reminder_set'", 'null': 'True', 'to': u"orm['introductions.IntroductionReminder']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['introductions.Person']"}),
            'requested': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'introductions.person': {
            'Meta': {'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preferred_email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'introductions.personcomment': {
            'Meta': {'object_name': 'PersonComment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_comment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_comment_set'", 'null': 'True', 'to': u"orm['introductions.PersonComment']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['introductions.Person']"})
        },
        u'introductions.personemail': {
            'Meta': {'object_name': 'PersonEmail'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'extracted_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['introductions.Person']", 'null': 'True'})
        },
        u'introductions.taggedintroduction': {
            'Meta': {'object_name': 'TaggedIntroduction'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['introductions.Introduction']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'introductions_taggedintroduction_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['introductions']