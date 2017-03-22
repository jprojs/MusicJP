from django.db import models


class Album(models.Model):
    albumid = models.AutoField(db_column='AlbumId', primary_key=True)
    title = models.CharField(max_length=200, db_column='Title')
    artistid = models.ForeignKey('Artist', db_column='ArtistId')

    class Meta:
        managed = False
        db_table = 'Album'


class Artist(models.Model):
    artistid = models.AutoField(db_column='ArtistId', primary_key=True)
    name = models.TextField(db_column='Name')

    class Meta:
        managed = False
        db_table = 'Artist'

    def short_name(self):

        if len(self.name) > 20:
            return self.name[:-5] + "..."
        else:
            return self.name


class Playlist(models.Model):
    playlistid = models.AutoField(db_column='PlaylistId', primary_key=True)
    name = models.TextField(db_column='Name')

    class Meta:
        managed = False
        db_table = 'Playlist'


class PlaylistTrack(models.Model):
    playlist = models.OneToOneField('Playlist', primary_key=True, db_column='PlayListId')
    track = models.OneToOneField('Track', primary_key=True, db_column='TrackId')

    class Meta:
        unique_together = ('playlist', 'track')
        managed = False
        db_table = 'PlayListTrack'


class MediaType(models.Model):
    mediatypeid = models.AutoField(db_column='MediaTypeId', primary_key=True)
    name = models.TextField(db_column='Name')

    class Meta:
        managed = False
        db_table = 'MediaType'


class Track(models.Model):
    trackid = models.AutoField(db_column='TrackId', primary_key=True)
    name = models.CharField(max_length=200, db_column='Name')
    albumid = models.ForeignKey('Album', db_column='AlbumId')
    mediatypeid = models.ForeignKey('MediaType', db_column='MediaTypeId')
    genreid = models.ForeignKey('Genre', db_column='GenreId')
    composer = models.CharField(max_length=200, db_column='Composer')
    milliseconds = models.IntegerField(db_column='Milliseconds')
    bytes = models.IntegerField(db_column='Bytes')
    unitPrice = models.CharField(max_length=200, db_column='UnitPrice')

    class Meta:
        managed = False
        db_table = 'Track'


class Genre(models.Model):
    genreid = models.AutoField(db_column='GenreId', primary_key=True)
    name = models.TextField(db_column='Name')

    class Meta:
        managed = False
        db_table = 'Genre'


class Customer(models.Model):
    customerid = models.AutoField(db_column='CustomerId', primary_key=True)
    firstname = models.CharField(max_length=200, db_column='FirstName')
    lastname = models.CharField(max_length=200, db_column='LastName')
    company = models.CharField(max_length=200, db_column='Company')
    address = models.CharField(max_length=200, db_column='Address')
    city = models.CharField(max_length=200, db_column='City')
    state = models.CharField(max_length=200, db_column='State')
    country = models.CharField(max_length=200, db_column='Country')
    postalcode = models.CharField(max_length=200, db_column='PostalCode')
    phone = models.CharField(max_length=200, db_column='Phone')
    fax = models.CharField(max_length=200, db_column='Fax')
    email = models.CharField(max_length=200, db_column='Email')
    supportRep = models.ForeignKey('Employee', db_column='SupportRepId')

    class Meta:
        managed = False
        db_table = 'Customer'


class Employee(models.Model):

    id = models.AutoField(db_column='EmployeeId', primary_key=True)
    lastname = models.CharField(max_length=200, db_column='LastName')
    firstname = models.CharField(max_length=200, db_column='FirstName')
    title = models.CharField(max_length=200, db_column='Title')
    reports_to = models.ForeignKey('Employee', db_column='ReportsTo')
    birthdate = models.DateTimeField(db_column='BirthDate')
    hiredate = models.DateTimeField(db_column='HireDate')
    address = models.CharField(max_length=200, db_column='Address')
    city = models.CharField(max_length=200, db_column='City')
    state = models.CharField(max_length=200, db_column='State')
    country = models.CharField(max_length=200, db_column='Country')
    postalcode = models.CharField(max_length=200, db_column='PostalCode')
    phone = models.CharField(max_length=200, db_column='Phone')
    fax = models.CharField(max_length=200, db_column='Fax')
    email = models.CharField(max_length=200, db_column='Email')

    class Meta:
        managed = False
        db_table = 'Employee'


class Invoice(models.Model):

    invoiceid = models.AutoField(db_column='InvoiceId', primary_key=True)
    customer = models.ForeignKey('Customer', db_column='CustomerId')
    invoicedate = models.DateTimeField(db_column='InvoiceDate')
    billingaddress = models.CharField(max_length=200, db_column='BillingAddress')
    billingcity = models.CharField(max_length=200, db_column='BillingCity')
    billingstate = models.CharField(max_length=200, db_column='BillingState')
    billingcountry = models.CharField(max_length=200, db_column='BillingCountry')
    billingpostalcode = models.CharField(max_length=200, db_column='BillingPostalCode')
    total = models.TextField(db_column='Total')

    class Meta:
        managed = False
        db_table = 'Invoice'


class Invoiceline(models.Model):
    invoicelineid = models.AutoField(db_column='InvoiceLineId', primary_key=True)
    invoice = models.ForeignKey('Invoice', db_column='InvoiceId')
    track = models.ForeignKey('Track', db_column='TrackId')
    unit_price = models.CharField(max_length=200, db_column='UnitPrice')
    quantity = models.CharField(max_length=200, db_column='Quantity')

    class Meta:
        managed = False
        db_table = 'InvoiceLine'




