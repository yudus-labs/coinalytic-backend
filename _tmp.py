from pathlib import Path
import yfolio.db as db

cfg_path = Path(__file__).parent.joinpath('.cfg', 'config.yml')
db.connect(cfg_path)

# details = db.TokenDetails(
#     homepage='homepage',
#     cap=0,
#     diluted_cap=0,
#     supply=0,
#     total_supply=0,
#     max_supply=0,
#     desc='desc',
#     links='links',
# )
# token = db.Tokens(
#     cg_id='cg_id',
#     logo='logo',
#     symbol='symbol',
#     name='name1',
#     price=0,
#     price_change_24h=0,
#     atl=0,
#     ath=0,
#     plo='plo',
#     tags=['tags1', 'tags2'],
#     w3f='w3f',
#     rank=0,
#     details=details,
# )
# token.save()

for t in db.Tokens.objects():
    print(t.name)