from pathlib import Path
import yfolio as pib
from yfolio import router

cfg_path = Path(__file__).parent.joinpath('.cfg', 'config.yml')

app = pib.create_app(cfg_path)
router.attach(app)


if __name__ == '__main__':
    app.run()
