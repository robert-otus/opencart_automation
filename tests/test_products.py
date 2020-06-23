def test_login(app):
    app.login.login_complete(username='user', password='bitnami1')
    assert app.driver.title == 'Dashboard'


def test_catalogue(app):
    app.login.login_complete(username='user', password='bitnami1')
    #assert app.driver.title == 'Dashboard'
    app.main.cat_list()
    assert app.driver.title == "Products"


def test_add_product(app):
    app.login.login_complete(username='user', password='bitnami1')
    app.main.cat_list()
    app.product.add_product(name='RMonitor', tag='RM', model='R-1')
    assert "Success: You have modified products!"


def test_edit_product(app):
    app.login.login_complete(username='user', password='bitnami1')
    app.main.cat_list()
    app.product.edit_product(price='11.11')
    assert "Success: You have modified products!"


def test_del_product(app):
    app.login.login_complete(username='user', password='bitnami1')
    app.main.cat_list()
    app.product.delete_product()
    assert "Success: You have modified products!"


def test_filter_pos(app):
    app.login.login_complete(username='user', password='bitnami1')
    app.main.cat_list()
    app.product.filter(prod='ipod nano')
    assert "Showing 1 to 1"


def test_filter_neg(app):
    app.login.login_complete(username='user', password='bitnami1')
    app.main.cat_list()
    app.product.filter(prod='ipod robert')
    assert "Showing 0 to 0"


def test_copy_product(app):
    app.login.login_complete(username='user', password='bitnami1')
    app.main.cat_list()
    app.product.copy_product()
    assert "Success: You have modified products!"


def test_orders(app):
    app.login.login_complete(username='user', password='bitnami1')
    app.order.check_orders()
    assert "No results!"


def test_reports(app):
    app.login.login_complete(username='user', password='bitnami1')
    app.report.check_reports()
    assert app.driver.title == "Reports"






