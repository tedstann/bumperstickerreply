from bumperstickerreply import db, Sticker
import datetime



cat = Sticker(
    photo='http://www.medhatspca.ca/sites/default/files/news_photos/2014-Apr-15/node-147/cute-little-cat.jpg',
    initial_comment='Look at the kitty!',
    comments=[
        {
            'text': 'That is indeed a kitten',
            'created': datetime.datetime.utcnow().isoformat()
        }
    ],
    tag='animals',
    view_count=0,
    created=datetime.datetime.utcnow()
)

zombie = Sticker(
    photo='http://rlv.zcache.com/road_sign_zombie_crossing_car_bumper_sticker-r0de541e440dc439f9dcc78e9f9343590_v9wht_8byvr_512.jpg',
    initial_comment='braiiinsss',
    comments=[],
    tag='zombies',
    view_count=12,
    created=datetime.datetime.utcnow()
)
db.session.add(cat)
db.session.add(zombie)
db.session.commit()
