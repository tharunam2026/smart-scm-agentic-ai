import React,{useEffect,useState} from 'react'
import{createRoot}from'react-dom/client'
import{Activity,AlertTriangle,Bot,Boxes,PackageCheck,RefreshCw,Send,Truck}from'lucide-react'
import'./styles.css'

const API='http://127.0.0.1:8000/api'
function App(){
 const[data,setData]=useState(null),[chat,setChat]=useState(''),[messages,setMessages]=useState([{role:'ai',text:'Hi! I am your SCM Decision Assistant. Ask about inventory, suppliers, risks or procurement.'}])
 const load=async()=>{try{setData(await(await fetch(API+'/dashboard')).json())}catch{alert('Start FastAPI on port 8000 first.')}}
 useEffect(()=>{load()},[])
 const ask=async()=>{if(!chat.trim())return;const q=chat;setMessages(m=>[...m,{role:'user',text:q}]);setChat('');try{const r=await fetch(API+'/ai/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:q})});const j=await r.json();setMessages(m=>[...m,{role:'ai',text:j.answer}])}catch{setMessages(m=>[...m,{role:'ai',text:'Backend connection failed.'}])}}
 if(!data)return <div className="loading"><Activity/> Loading Smart SCM...</div>
 const k=data.kpis
 return <div className="app">
  <aside className="sidebar"><div className="brand"><div className="logo">S</div><div><b>Smart SCM</b><span>Agentic AI</span></div></div>
   <nav><a className="active">Dashboard</a><a>Inventory</a><a>Procurement</a><a>Suppliers</a><a>Risk Monitor</a></nav>
   <div className="agent-box"><Bot size={20}/><div><b>AI Agents Online</b><small>6 decision agents</small></div></div>
  </aside>
  <main className="main"><header><div><h1>Supply Chain Command Center</h1><p>Observe → Analyze → Reason → Decide</p></div><button className="refresh" onClick={load}><RefreshCw size={17}/> Refresh</button></header>
   <section className="cards"><K icon={<Boxes/>} l="Inventory Value" v={'₹'+Number(k.inventory_value).toLocaleString()}/><K icon={<PackageCheck/>} l="Products" v={k.products}/><K icon={<AlertTriangle/>} l="Critical Items" v={k.critical_items} d/><K icon={<Truck/>} l="Open Orders" v={k.pending_orders}/></section>
   <section className="grid">
    <div className="panel"><Head t="Inventory Intelligence" s="Agent-generated stock health"/><table><thead><tr><th>SKU</th><th>Product</th><th>Stock</th><th>Days</th><th>Status</th></tr></thead><tbody>{data.inventory.map(x=><tr key={x.sku}><td>{x.sku}</td><td>{x.product_name}</td><td>{x.stock}</td><td>{x.days_of_stock}</td><td><span className={'pill '+x.status.toLowerCase()}>{x.status}</span></td></tr>)}</tbody></table></div>
    <div className="panel"><Head t="AI Action Plan" s="Decision Agent output" icon={<Bot/>}/><div className="actions">{data.actions.map((a,i)=><div className="action" key={i}><span className={'priority '+a.priority.toLowerCase()}>{a.priority}</span><b>{a.action}</b><small>{a.sku} · {a.supplier}</small><small>{a.why}</small></div>)}</div></div>
    <div className="panel"><Head t="Supply Chain Risks" s="Risk Agent monitoring" icon={<AlertTriangle/>}/>{data.risks.length?data.risks.map((r,i)=><div className="risk" key={i}><div className="dot"/><div><b>{r.sku} — {r.risk} Risk</b><span>{r.message} Best supplier: {r.best_supplier}</span></div></div>):<p>No current risks.</p>}</div>
    <div className="panel chat"><Head t="SCM AI Assistant" s="Ask the agents" icon={<Bot/>}/><div className="chat-messages">{messages.map((m,i)=><div key={i} className={'msg '+m.role}>{m.text}</div>)}</div><div className="chat-input"><input value={chat} onChange={e=>setChat(e.target.value)} onKeyDown={e=>e.key==='Enter'&&ask()} placeholder="e.g. Which supplier should I choose?"/><button onClick={ask}><Send size={17}/></button></div></div>
   </section>
  </main></div>
}
function K({icon,l,v,d}){return <div className="kpi"><div className="ki">{icon}</div><div><span>{l}</span><strong className={d?'danger':''}>{v}</strong></div></div>}
function Head({t,s,icon}){return <div className="head"><div><h2>{t}</h2><p>{s}</p></div>{icon}</div>}
createRoot(document.getElementById('root')).render(<App/>)
