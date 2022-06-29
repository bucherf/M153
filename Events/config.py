from configparser import ConfigParser

def dbConfig(filename='database.ini',section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    dbConfigs = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            dbConfigs[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in {1}'.format(section,filename))

    return dbConfigs

dbConfig()