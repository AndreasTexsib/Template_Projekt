from flask import Blueprint, render_template

from src.util.log_util import log_print

bp = Blueprint(
    name="blueprint", import_name=__name__, url_prefix="/blueprint"
)

@bp.get("/")
def index():
    log_print("Blueprints aufgerufen")
    return render_template(
        "index.html.j2",
        title = "Blueprint"    
    )