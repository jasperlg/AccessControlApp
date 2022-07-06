from data.dbsetup.migrations import createDBTables, removeDBTables
from data.dbsetup.seeds import seedDB

removeDBTables()
createDBTables()
seedDB()
