from pages.desktop.mission import MissionPage
from unittestzero import Assert


class TestMissionPage:

    def test_sidebar_links(self, mozwebqa):
        missionPage = MissionPage(mozwebqa)
        missionPage.go_to_page()
        Assert.true(missionPage.are_sidebar_links_present)
        Assert.true(missionPage.are_breadcrumb_links_present)
        Assert.true(missionPage.are_learn_more_links_present)

    def test_header_section_present(self, mozwebqa):
        missionPage = MissionPage(mozwebqa)
        missionPage.go_to_page()
        missionPage.toggle_tabzilla_dropdown()
        Assert.equal(missionPage.are_tabzilla_links_present, True)

    def test_footer_section_present(self, mozwebqa):
        missionPage = MissionPage(mozwebqa)
        missionPage.go_to_page()
        Assert.equal(missionPage.are_footer_links_present, True)
