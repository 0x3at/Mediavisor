from ..ext.database import DB as db

media_server_association_table = db.Table(
    "movie_server_association",
    db.Column("media_id", db.Integer, db.ForeignKey("media.id")),
    db.Column("server_id", db.Integer, db.ForeignKey("server.id")),
)
