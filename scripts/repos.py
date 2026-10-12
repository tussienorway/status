import json,subprocess,datetime
d=json.load(open('status.json'));out=[]
for r in ['majere-core','majere-site','majere-research','huggingface']:
  try:
    c=json.loads(subprocess.check_output(['gh','api',f'repos/tussienorway/{r}/commits?per_page=1']))
    if c: out.append({'repo':r,'title':c[0]['commit']['message'].split('\n')[0][:80],'time':c[0]['commit']['committer']['date'],'url':c[0]['html_url']})
  except Exception: pass
d['repos']=out;d['updated']=datetime.datetime.now(datetime.timezone.utc).isoformat()
json.dump(d,open('status.json','w'),ensure_ascii=False,indent=1)
