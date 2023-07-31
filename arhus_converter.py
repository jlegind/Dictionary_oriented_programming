import pandas as pd
import shelve

df = pd.read_excel(r'C:\Users\bxq762\Desktop\protoType\Aarhus.xls')

hdrs = [j for j in df.columns]

id = list(df.Sortnr)
rank = list(df.TYPE)
tname = list(df.NAME)
print('len list ID =', len(id))

zp = zip(id, rank, tname)

subdf = list(zp)
zp = subdf[0:20]
# superfamily = ''
# family = ''
# genus = ''
def parseTaxonomy(taxon_input):
    #Format must be ID, rank, name data structure
    #Returns one record at a time. User must handle that atomic record until nested function becomes available
    taxon_input = taxon_input
    taxonomy = {
        "superfamily":[{"name":"supfam"}],
        "family":[{"name":"famil", "parent":"superfamily"}],
        "genus":[{"name":"genus", "parent":"famil"}],
        "species":[{"name":"species", "parent":"genus"}]
    }
    appRecord = {'sortnr':0, 'superfamily': '', 'family': '', 'genus':'', 'species':''} #Might need 'parent':parentID
    # group = []
    # appRecord['sortnr'] = taxon_input[0]
    # if taxon_input[1] == 'supfam':
    #     superfamily = taxon_input[2]
    # if taxon_input[1] == 'famil':
    #     family = taxon_input[2]
    # if taxon_input[1] == 'genus':
    #     genus = taxon_input[2]
    # appRecord['superFamily'] = superfamily
    # appRecord['family'] = family
    # appRecord['genus'] = genus
    # appRecord['species'] =
    ikea =  shelve.open('ikea', writeback=True)
    record = {'superfamily' : '', 'family' : '', 'genus':'', 'species' : ''}

    ikea['record'] = record
    print('tax inp=', taxon_input)
    innerRecord = {'superfamily': '', 'family': '', 'genus': '', 'species': ''}
    ikea['inner'] = innerRecord

    def inner_taxonRecord(arhusUnit):
        #Processes atomic unit

        sortnr = arhusUnit[0]
        recordReset = {'superfamily': '', 'family': '', 'genus': '', 'species': ''}
        # innerDict = {'id':sortnr, 'innerrecord':innerRecord}
        # ikea[sortnr][innerRecord]
        # ikea[sortnr]['sort']
        superFamily = ''
        family = ''
        # genus = ''

        if j[1] == 'supfam':
            if superFamily != j[2]:
                superFamily = j[2]
                ikea['inner'] = recordReset
                print('new superfam = ', superFamily)
            # ikea[sortnr]['superfamily'] = superFamily
            ikea['inner']['superfamily'] = superFamily
            print('supfam =', superFamily)


        else:
            superFamily = ' '
        # ikea[sortnr]['superfamily'] = superFamily
        #     innerRecord['superfamily'] = ' '
        if j[1] == 'famil':
            family = j[2]
            print('INNER', ikea['inner'], family)
            ikea['inner']['family'] = family
        else:
            family = ' '
            # innerRecord['family'] = ' '
        # ikea[sortnr]['family'] = family
        print('family =', family)
        if j[1] == 'genus':
            genus = j[2]
            ikea['inner']['genus'] = genus
        else:
            genus = ''
        # ikea[sortnr]['genus'] = genus
        #     innerRecord['genus'] = ' '
        if j[1] == 'species':
            species = j[2]
            ikea['inner']['species'] = species
        else:
            species = ' '
            # innerRecord['species'] = ' '
        # ikea[sortnr]['species'] = species

        print('#####', ikea['inner'], '£££££££')
        return ikea['inner']

    processedArhus = []


    for j in taxon_input:
        res = inner_taxonRecord(j)
        print(res)
        processedArhus.append(res)
        # res = f"sortnr={j[0]}, rank={j[1]}, sortnr type = {type(j[0])}"
        # print(res)
        # if j[0] == '200':
        #     print('TRying to beak!')
        #     break


q = parseTaxonomy(zp)
# counter = 20
# end_recordList = []
# while counter:
#     for j in zp:
#         rec = parseTaxonomy(j)
#         print('j rec:', rec)
#         end_recordList.append(rec)
#         # print('sortnr. ::', j[0])
#         counter -= 1
#         if counter == 0:
#             break
#
# print('######', end_recordList, '####')

