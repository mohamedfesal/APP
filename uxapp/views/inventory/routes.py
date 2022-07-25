from flask import Blueprint, redirect, render_template, request, session, url_for, flash
from flask_login import current_user, login_required
from uxapp.models import Agents, Stock_cat, Stock, Orders
from uxapp.functions import required_roles
from uxapp import db

inventory_routes = Blueprint('inventory_routes', __name__)

@inventory_routes.route("/inventory" , methods=['GET', 'POST'])
@login_required
def stock():
    if request.method == "POST":
        pass
    return render_template('/inventory/inventory.html')