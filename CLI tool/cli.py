import argparse

def create_parse():
    parser=argparse.ArgumentPArser()
    parser.add_argument('--patth', help=='the path to the export file')
    parser.add_argumet('--format',default='json',choices=['json','csv'],type=str.lower)
    return parser

def main():
    import sys
    from hr import export
    from hr import user as us

    args=create_parser().parse_args()
    users=u.fetch_users()

    if args.path:
        file=open(args.path,'w',newline='')
    else:
        file=sys.stdout
    
    if args.format=='json':
        export.to_json_file(file,users)
    else: 
        export.to_csv_file(file,users)
