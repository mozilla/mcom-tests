import pytest
from pages.desktop.mission import Mission
from unittestzero import Assert


class TestMissionPage:

    @pytest.mark.nondestructive
    def test_sidebar_links(self, mozwebqa):
        missionPage = Mission(mozwebqa)
        missionPage.go_to_page()
        Assert.true(missionPage.are_sidebar_links_visible)
        Assert.true(missionPage.are_breadcrumb_links_visible)
        Assert.true(missionPage.are_learn_more_links_visible)

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        Assert.true(mission_page.footer.are_footer_links_visible)

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        Assert.true(mission_page.header.is_tabzilla_panel_visible)
        mission_page.header.toggle_tabzilla_dropdown()
        Assert.true(mission_page.header.are_tabzilla_links_visible)
