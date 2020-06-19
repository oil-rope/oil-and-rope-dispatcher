from oilandrope_dispatcher.routes import dashboard


def test_dashboard():
    assert dashboard.dashboard() == '<h1>Dashboard</h1>'
