# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################
import datetime
    
def post_Add():
    form=SQLFORM(db.advertise)
    form.vars.add_type="sell"
    form.vars.status="open"
    form.vars.ppl_bid=0
   # form=form.process(next='index')
    form=form.process()
    if form.accepted:
        session.flash="Posted Successfully"
        redirect(URL('index'))
    #db.advertise.post_date=request.now()
    return locals()


def view_Add():
    #auth_user_with_role = db(db.auth_membership.group_id==request.vars.role).select(d
    #rows=db(db.advertise.id==request.args(0)).select()
    ############bidding_rows=db(db.bidding.add_id==request.args(0)).select()
    query=(db.bidding.add_id==request.args(0)) & (db.advertise.id==request.args(0))
    rows=db(db.advertise.id==request.args(0)).select()
    bidder_rows=db(query).select()
    bid_form=SQLFORM(db.bidding)
    bid_form.vars.bidder_user_id=auth.user_id
    bid_form.vars.bidder_user_fn=auth.user.first_name
    bid_form.vars.bidder_user_ln=auth.user.last_name
    bid_form.vars.bid_datetime=datetime.datetime.utcnow()
    bid_form.vars.add_id=request.args(0,cast=int)
    bid_form.process()
    if bid_form.accepted:
        session.flash="Bidded Successfully"

    #bidder_rows=db(db.bidding.add_id==request.args(0)).select()
   # bidders_rows=db().select()
   # users = db(db.auth_user.id>=1).select(db.auth_user.ALL)
    #for user in users:
       # response.write(user.id)
       # user_rows=db(db.auth_user.id==user.id).select(db.auth_user.first_name)
    #    ad_rows=db(db.advertise.created_by==user.id).select()
   # user_name=db(db.advertise.created_by).select(auth_user.firstname)
    return locals()

@auth.requires_login()
def index():
    """
    
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    rows=db(db.advertise).select()
   # response.flash = T("Welcome to web2py!")
    return locals()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
