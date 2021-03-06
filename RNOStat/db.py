def build_models(db):
    class _KickLog(db.Model):
        __table_name__ = "kick_log"

        id = db.Column(db.Integer, primary_key=True)
        wallet = db.Column(db.String(128), nullable=False)
        weight = db.Column(db.Float, nullable=False)
        archi = db.Column(db.String(50), nullable=True)
        hertz = db.Column(db.Float, nullable=True)
        threads = db.Column(db.Integer, nullable=True)

        def __init__(self, wallet, weight, archi, hertz, threads):
            self.wallet = wallet
            self.weight = weight
            self.archi = archi      or None
            self.hertz = hertz      or None
            self.threads = threads   or None

        def __repr__(self):
            return f"<KickLog('{self.wallet}', '{self.weight}' with '{self.archi}', {self.hertz} x {self.thread})>"

    class Models:
        KickLog=_KickLog

    return Models

