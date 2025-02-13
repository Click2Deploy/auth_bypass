from odoo import http
from odoo.http import request

class AutoLogin(http.Controller):
    @http.route('/auth/bypass', type='http', auth='none', csrf=False)
    def auto_login(self, **kwargs):
        session_id = request.httprequest.args.get('session_id')
        if session_id:
            response = request.redirect('/web')
            response.set_cookie('session_id', session_id, path='/', httponly=True)
            return response  

        return request.redirect('/web/login')
