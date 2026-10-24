import subprocess, textwrap
BLUE="#0A5AC8"
def render(name, dot):
    open(name+".dot","w").write(dot)
    subprocess.run(["dot","-Tpng","-Gdpi=170",name+".dot","-o",name+".png"],check=True)

T = {
 "en": dict(
  ped="Pedestrian\n(student, resident, elderly,\nparent with stroller)", ext="External client\n(app, script)", res="Researcher /\nurban planner",
  sys="Shaded pedestrian\nrouting system\n(Go + Python)",
  osm="OpenStreetMap\n(road graph, buildings)", hts="Building height data\n(OSM / Astana open data)", tiles="Map tile\nprovider",
  uc=["Build a route","Set λ and detour limit","Compare 3 modes","Show shade on map","Export route","Load district data","Evaluate vs baseline"],
  web="Web client\n(MapLibre GL JS)", api="Go: REST API +\nrouting service", db="PostgreSQL + PostGIS\n(graph, buildings, edge_shade)",
  py="Python: shadow module\n(Shapely + pvlib)", ld="Python: OSM / height\nloader", ev="Evaluation scripts\n(eval/)", mem="in-memory graph\n+ per-slot weights", off="offline precompute",
  ctxt="System context", uct="Use cases", cmpt="Components (draft)"),
}
for L,t in T.items():
    node='fontname="DejaVu Sans" fontsize=12 style="filled,rounded" shape=box penwidth=1.4'
    # context
    render(f"ctx_{L}", f'''digraph G {{ rankdir=LR; nodesep=0.35; ranksep=0.9; node [{node}]; edge [fontname="DejaVu Sans" fontsize=10 color="#555555"];
 ped [label="{t['ped']}" fillcolor="#E8F0FC" color="{BLUE}"]; ext [label="{t['ext']}" fillcolor="#E8F0FC" color="{BLUE}"]; res [label="{t['res']}" fillcolor="#E8F0FC" color="{BLUE}"];
 sys [label="{t['sys']}" fillcolor="{BLUE}" fontcolor=white fontsize=14 color="{BLUE}"];
 osm [label="{t['osm']}" fillcolor="#F2F2F2" color="#888888"]; hts [label="{t['hts']}" fillcolor="#F2F2F2" color="#888888"]; tiles [label="{t['tiles']}" fillcolor="#F2F2F2" color="#888888"];
 ped -> sys; ext -> sys; res -> sys; osm -> sys; hts -> sys; tiles -> sys [dir=both]; }}''')
    # use case
    ucs=t['uc']
    lines=['digraph G { rankdir=LR; nodesep=0.25; ranksep=1.6; node [fontname="DejaVu Sans" fontsize=12]; edge [color="#555555" arrowhead=none];',
      f'ped [label="{t["ped"].splitlines()[0]}" shape=box style="filled,rounded" fillcolor="#E8F0FC" color="{BLUE}"];',
      f'ext [label="{t["ext"].splitlines()[0]}" shape=box style="filled,rounded" fillcolor="#E8F0FC" color="{BLUE}"];',
      f'res [label="{t["res"].replace(chr(10)," ")}" shape=box style="filled,rounded" fillcolor="#E8F0FC" color="{BLUE}"];',
      'subgraph cluster_s { label="'+t['sys'].replace("\n"," ")+'"; fontname="DejaVu Sans"; color="'+BLUE+'"; style=rounded;']
    for i,u in enumerate(ucs): lines.append(f'u{i} [label="{u}" shape=ellipse style=filled fillcolor="#FFFFFF" color="{BLUE}"];')
    lines.append('}')
    for i in (0,1,2,3,4): lines.append(f'ped -> u{i};')
    for i in (0,3,4): lines.append(f'ext -> u{i};')
    for i in (5,6): lines.append(f'res -> u{i};')
    lines.append('}')
    render(f"uc_{L}", "\n".join(lines))
    # components
    render(f"cmp_{L}", f'''digraph G {{ rankdir=TB; nodesep=0.5; ranksep=0.7; node [{node}]; edge [fontname="DejaVu Sans" fontsize=10 color="#555555"];
 web [label="{t['web']}" fillcolor="#E8F0FC" color="{BLUE}"];
 api [label="{t['api']}" fillcolor="{BLUE}" fontcolor=white color="{BLUE}"];
 mem [label="{t['mem']}" shape=note fillcolor="#FFFFFF" color="{BLUE}"];
 db [label="{t['db']}" shape=cylinder fillcolor="#FFF4D6" color="#B8860B"];
 py [label="{t['py']}" fillcolor="#DFF3E3" color="#2E7D32"]; ld [label="{t['ld']}" fillcolor="#DFF3E3" color="#2E7D32"];
 ev [label="{t['ev']}" fillcolor="#F2F2F2" color="#888888"]; osm [label="OSM / heights" shape=box fillcolor="#F2F2F2" color="#888888"];
 web -> api [label="REST / GeoJSON"]; ev -> api [label="REST"]; api -> mem [style=dashed]; api -> db [label="load (start / update)"];
 osm -> ld; ld -> db; py -> db [label="edge_shade(slot)"]; db -> py [label="buildings"]; {{rank=same; py; ld; }} }}''')
print("ok")
