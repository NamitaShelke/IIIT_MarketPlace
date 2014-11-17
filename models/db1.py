# -*- coding: utf-8 -*-
#db.define_table('advertise',
 #               Field('add_id','integer',readable=False,writable=False),
  #              Field('item_name','string',requires=IS_NOT_EMPTY()),
   #             Field('category','string',requires=IS_NOT_EMPTY()),
    #            Field('user_name','string',requires=IS_NOT_EMPTY(),readable=False,writable=False),
     #           Field('add_type','string',requires=IS_NOT_EMPTY(),readable=False,writable=False),
      #          Field('status','string',requires=IS_NOT_EMPTY(),readable=False,writable=False),
       #         Field('post_date','date',requires=IS_NOT_EMPTY(),readable=False,writable=False),
        #        Field('ppl_bid','integer',readable=False,writable=False),
         #       Field('item_img','upload'))

db.define_table('advertise',
               # Field('add_id','integer',readable=False,writable=False),
                Field('item_name','string',requires=IS_NOT_EMPTY()),
                Field('category','string',requires=IS_NOT_EMPTY()),
               # Field('user_name','reference auth_user',readable=False,writable=False),
                Field('add_type','string',requires=IS_NOT_EMPTY(),readable=False,writable=False),
                Field('status','string',requires=IS_NOT_EMPTY(),readable=False,writable=False),
                #Field('post_date','datetime',requires=IS_NOT_EMPTY(),readable=False,writable=False),
                Field('ppl_bid','integer',readable=False,writable=False),
                #Field('item_img','upload'),
               Field('item_img','upload',uploadfield="myblob"),Field('myblob','blob',default=''),
                auth.signature)
