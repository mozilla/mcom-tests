from unittestzero import Assert
from pages.desktop.technology_page import TechnologyPage


class TestTechnologyPage:

    @pytest.mark.nondestructive
    def test_header_section_visible(self, mozwebqa):
        technology_page = TechnologyPage(mozwebqa)
        technology_page.go_to_page()
        technology_page.toggle_tabzilla_dropdown()
        Assert.equal(technology_page.are_tabzilla_links_visible, True)

    @pytest.mark.nondestructive
    def test_footer_section_visible(self, mozwebqa):
        technology_page = TechnologyPage(mozwebqa)
        technology_page.go_to_page()
        Assert.equal(technology_page.are_footer_links_visible, True)

    @pytest.mark.nondestructive
    def test_billboard_links_are_visible(self, mozwebqa):
        technology_page = TechnologyPage(mozwebqa)
        technology_page.go_to_page()
        Assert.equal(technology_page.are_billboard_links_visible, True)
