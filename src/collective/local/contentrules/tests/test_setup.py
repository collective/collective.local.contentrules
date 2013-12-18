# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.local.contentrules.contentrules.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of collective.local.contentrules.contentrules into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.local.contentrules.contentrules is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.local.contentrules.contentrules'))

    def test_uninstall(self):
        """Test if collective.local.contentrules.contentrules is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.local.contentrules.contentrules'])
        self.assertFalse(self.installer.isProductInstalled('collective.local.contentrules.contentrules'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollective.local.contentrulesContentrulesLayer is registered."""
        from collective.local.contentrules.contentrules.interfaces import ICollective.local.contentrulesContentrulesLayer
        from plone.browserlayer import utils
        self.assertIn(ICollective.local.contentrulesContentrulesLayer, utils.registered_layers())
