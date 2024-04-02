import pkg_resources

def path_to_resource(filename: str) -> str:
    return pkg_resources.resource_filename('techbyai', f'resources/{filename}')
