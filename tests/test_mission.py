from pages.desktop.mission import MissionPage
from unittestzero import Assert


class TestMissionPage:

    def test_sidebar_links(self, mozwebqa):
        missionPage = MissionPage(mozwebqa)
        missionPage.go_to_page()
        Assert.true(missionPage.are_sidebar_links_visible)
        Assert.true(missionPage.are_breadcrumb_links_visible)
        Assert.true(missionPage.are_learn_more_links_visible)

    def test_header_section_present(self, mozwebqa):
        missionPage = MissionPage(mozwebqa)
        missionPage.go_to_page()
        missionPage.toggle_tabzilla_dropdown()
        Assert.true(missionPage.are_tabzilla_links_present)

    def test_footer_section_present(self, mozwebqa):
        missionPage = MissionPage(mozwebqa)
        missionPage.go_to_page()
        Assert.true(missionPage.are_footer_links_present)
