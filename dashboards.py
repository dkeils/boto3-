import boto3
# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')



{
    'DashboardArn': 'arn:aws:cloudwatch::670606342645:dashboard/Webserver-Memory-History',
    'DashboardBody': '{"widgets":[{"type":"metric","x":0,"y":0,"width":24,"height":12,"properties":{"metrics":[["CWAgent","mem_used_percent","InstanceId","i-088f667b6b554de9b","ImageId","ami-0323c3dd2da7fb37d","InstanceType","t3.medium",{"label":"web01.cne) t3.medium"}],["...","i-0eb56c3e18eac78ec",".",".",".",".",{"label":"web01.espeed) t3.medium"}],["...","i-0a90ca760315f6f88",".",".",".",".",{"label":"web02.espeed) t3.medium"}],["...","i-0ae3021b9da0a6ab0",".","ami-09d95fab7fff3776c",".",".",{"label":"web01.flexdeploys) t3.medium"}],["...","i-0f144fc6ad5a9b277",".","ami-0323c3dd2da7fb37d",".","r5.large",{"label":"web01.gd) r5.large"}],["...","i-0202527a3d9ee0a83",".",".",".","t3.medium",{"label":"web01.inland) t3.medium"}],["...","i-045a360960451b33c",".",".",".","r5.large",{"label":"web01.insitewireless) r5.large"}],["...","i-0b7a7dd0746679579",".",".",".",".",{"label":"web02.insitewireless) r5.large"}],["...","i-071d0d3eaafda05b9",".",".",".","t3.medium",{"label":"web01.iota) t3.medium"}],["...","i-093a682c9e0d9828f",".",".",".",".",{"label":"web01.keytower) t3.medium"}],["...","i-05bb26620043703e5",".","ami-09d95fab7fff3776c",".","r5.large",{"label":"web01.mobilitie) r5.large"}],["...","i-0e64a9a66742fe711",".",".",".",".",{"label":"web02.mobilitie) r5.large"}],["...","i-0e86b9d36d87e6ba6",".","ami-0323c3dd2da7fb37d",".","t3.medium",{"label":"web01.nextlink) t3.medium"}],["...","i-0515897ccffa4b563",".","ami-09d95fab7fff3776c",".",".",{"label":"web01.pyramidns) t3.medium"}],["...","i-08d97d99060dfa3d3",".","ami-0323c3dd2da7fb37d",".",".",{"label":"web01.samsung) t3.medium"}],["...","i-07230e6ef86e176fb",".","ami-09d95fab7fff3776c",".","r5.large",{"label":"web01.sba) r5.large"}],["...","i-0dc2911923991467c",".",".",".",".",{"label":"web02.sba) r5.large"}],["...","i-00d238c2a2baaefe8",".","ami-0323c3dd2da7fb37d",".","t3.medium",{"label":"web01.smartworks) t3.medium"}],["...","i-0d160c45d557d250c",".","ami-08f3d892de259504d",".",".",{"label":"web02.smartworks"}],["...","i-0787df807554c8659",".","ami-0323c3dd2da7fb37d",".",".",{"label":"web01.smj) t3.medium"}],["...","i-0432928afee4d2ff9",".",".",".",".",{"label":"web01.southerntowers) t3.medium"}],["...","i-0cc78026c99cdbcef",".",".",".","t3.large",{"label":"web01.starry) t3.large"}],["...","i-0839afe6b5650ded0",".",".",".",".",{"label":"web01.trackor) t3.large"}],["...","i-0df4dafb4e8a9d12b",".",".",".","r5.large",{"label":"web01.turf-gd) r5.large"}],["...","i-05a842049d6290d06",".",".",".","t3.medium",{"label":"web01.uscc"}],["...","i-0eaf743dad1b0c87a",".",".",".","."],["...","i-0c8e5154b09534a1e",".","ami-02354e95b39ca8dec",".","."]],"view":"timeSeries","region":"us-east-1","period":300,"stat":"Maximum","stacked":false,"setPeriodToTimeRange":true,"legend":{"position":"right"}}}]}',
    'DashboardName': 'Webserver-Memory-History',
    'ResponseMetadata':
    {
        'RequestId': 'b0f42854-9e52-43ba-a7ba-e3098c400d52',
        'HTTPStatusCode': 200,
        'HTTPHeaders':
        {
            'x-amzn-requestid': 'b0f42854-9e52-43ba-a7ba-e3098c400d52',
            'content-type': 'text/xml',
            'content-length': '5568',
            'vary': 'accept-encoding',
            'date': 'Thu, 23 Sep 2021 13:37:31 GMT'
        },
        'RetryAttempts': 0
    }
}
