from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in einvoice_for_fuelants/__init__.py
from einvoice_for_fuelants import __version__ as version

setup(
	name="einvoice_for_fuelants",
	version=version,
	description="e-Invoicing for fuelants streamlines fuel transaction management by automating GST-compliant invoicing and connecting directly to e-Invoice registration portals. With this feature, users can configure fuel items, set up GST details, and automatically calculate taxes based on item specifications. Each e-Invoice generates an IRN (Invoice Reference Number) and a QR code upon submission, meeting regulatory standards. Additionally, ERPNext provides downloadable PDFs for easy record-keeping, along with automated reports to track invoice status and ensure compliance. This setup minimizes manual data entry and enhances efficiency for organizations handling high-volume fuel transactions.",
	author="SVNIX Solutions",
	author_email="contact@svnix.solutions",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
