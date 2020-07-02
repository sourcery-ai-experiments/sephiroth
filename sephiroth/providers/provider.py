from sephiroth.providers import AWS, Azure, GCP, OCI, ASN, File, Tor

classmap = {
    "aws": AWS,
    "azure": Azure,
    "gcp": GCP,
    "oci": OCI,
    "asn": ASN,
    "file": File,
    "tor": Tor,
}


class Provider:
    def __init__(self, provider, targets_in=None):
        if targets_in:
            self.provider = classmap[provider](targets_in)
        else:
            self.provider = classmap[provider]()

    def get_processed_ranges(self):
        return self.provider.get_processed_ranges()