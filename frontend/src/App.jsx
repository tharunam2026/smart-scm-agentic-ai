import React from 'react';

export default function App() {
  return (
    <div style={{ fontFamily: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif', backgroundColor: '#f4f6f9', minHeight: '100vh', padding: '20px' }}>
      {/* Header */}
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', backgroundColor: '#fff', padding: '20px 30px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)', marginBottom: '20px' }}>
        <div>
          <h1 style={{ margin: 0, color: '#1e293b', fontSize: '24px' }}>Smart SCM — Agentic AI Textile System</h1>
          <p style={{ margin: '5px 0 0 0', color: '#64748b', fontSize: '14px' }}>Production Planning, Inventory & Dynamic Rescheduling Dashboard</p>
        </div>
        <div style={{ background: '#dcfce7', color: '#166534', padding: '8px 16px', borderRadius: '20px', fontWeight: 'bold', fontSize: '14px' }}>
          ● System Active & Connected
        </div>
      </header>

      {/* KPI Cards Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '20px', marginBottom: '30px' }}>
        <div style={{ background: '#fff', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)', borderLeft: '4px solid #3b82f6' }}>
          <h3 style={{ margin: '0 0 10px 0', color: '#64748b', fontSize: '14px' }}>Total Customer Orders</h3>
          <p style={{ margin: 0, fontSize: '28px', fontWeight: 'bold', color: '#1e293b' }}>12</p>
        </div>
        <div style={{ background: '#fff', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)', borderLeft: '4px solid #eab308' }}>
          <h3 style={{ margin: '0 0 10px 0', color: '#64748b', fontSize: '14px' }}>Pending / In-Progress</h3>
          <p style={{ margin: 0, fontSize: '28px', fontWeight: 'bold', color: '#1e293b' }}>4</p>
        </div>
        <div style={{ background: '#fff', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)', borderLeft: '4px solid #ef4444' }}>
          <h3 style={{ margin: '0 0 10px 0', color: '#64748b', fontSize: '14px' }}>Delayed / Risk Orders</h3>
          <p style={{ margin: 0, fontSize: '28px', fontWeight: 'bold', color: '#ef4444' }}>1</p>
        </div>
        <div style={{ background: '#fff', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)', borderLeft: '4px solid #8b5cf6' }}>
          <h3 style={{ margin: '0 0 10px 0', color: '#64748b', fontSize: '14px' }}>Low Stock Materials</h3>
          <p style={{ margin: 0, fontSize: '28px', fontWeight: 'bold', color: '#8b5cf6' }}>3</p>
        </div>
      </div>

      {/* Main Content Sections */}
      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '20px' }}>
        <div style={{ background: '#fff', padding: '25px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
          <h2 style={{ margin: '0 0 20px 0', fontSize: '18px', color: '#1e293b' }}>Active Production Schedules & Rescheduling</h2>
          <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '14px' }}>
            <thead>
              <tr style={{ borderBottom: '2px solid #e2e8f0', color: '#64748b' }}>
                <th style={{ padding: '10px' }}>Order ID</th>
                <th style={{ padding: '10px' }}>Product Type</th>
                <th style={{ padding: '10px' }}>Quantity</th>
                <th style={{ padding: '10px' }}>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr style={{ borderBottom: '1px solid #f1f5f9' }}>
                <td style={{ padding: '12px', fontWeight: '500' }}>ORD-101</td>
                <td style={{ padding: '12px' }}>Cotton Yarn 40s</td>
                <td style={{ padding: '12px' }}>1,000 kg</td>
                <td style={{ padding: '12px' }}><span style={{ background: '#fef3c7', color: '#92400e', padding: '4px 8px', borderRadius: '4px', fontSize: '12px' }}>Pending</span></td>
              </tr>
              <tr style={{ borderBottom: '1px solid #f1f5f9' }}>
                <td style={{ padding: '12px', fontWeight: '500' }}>ORD-102</td>
                <td style={{ padding: '12px' }}>Denim Fabric</td>
                <td style={{ padding: '12px' }}>2,500 m</td>
                <td style={{ padding: '12px' }}><span style={{ background: '#dcfce7', color: '#166534', padding: '4px 8px', borderRadius: '4px', fontSize: '12px' }}>Completed</span></td>
              </tr>
              <tr>
                <td style={{ padding: '12px', fontWeight: '500' }}>ORD-103</td>
                <td style={{ padding: '12px' }}>Silk Blend Fabric</td>
                <td style={{ padding: '12px' }}>800 m</td>
                <td style={{ padding: '12px' }}><span style={{ background: '#fee2e2', color: '#991b1b', padding: '4px 8px', borderRadius: '4px', fontSize: '12px' }}>Delayed</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        {/* Agentic AI Status Panel */}
        <div style={{ background: '#fff', padding: '25px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
          <h2 style={{ margin: '0 0 15px 0', fontSize: '18px', color: '#1e293b' }}>🤖 Agentic AI Orchestrator</h2>
          <p style={{ fontSize: '13px', color: '#64748b', lineHeight: '1.5' }}>
            AI Agents are actively monitoring inventory shortages, machine breakdown risks, and rescheduling candidate schedules.
          </p>
          <div style={{ background: '#f8fafc', padding: '15px', borderRadius: '6px', border: '1px solid #e2e8f0', marginTop: '15px' }}>
            <p style={{ margin: '0 0 8px 0', fontSize: '13px', fontWeight: 'bold', color: '#334155' }}>⚡ Latest AI Recommendation:</p>
            <p style={{ margin: 0, fontSize: '12px', color: '#475569' }}>
              Reschedule ORD-103 to Loom-2 due to yarn delay. Expected saving: 14% waste reduction.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}