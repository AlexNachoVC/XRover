import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const PressureChartSmall = ({ data }) => {
  return (
    <div className="w-full h-full">
      <h2>Pressure Over Time</h2>
        <LineChart width={600} height={300} data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="timestamp" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="pressure" stroke="#82ca9d" />
        </LineChart>
    </div>
  );
};

export default PressureChartSmall;