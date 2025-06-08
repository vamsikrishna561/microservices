import { Option } from "@repo/ui/types/option";

const fetchCatalogTypes = async () : Promise<Option[]> => {
  try {
    const response = await fetch('http://localhost:8080/product/types');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching catalog types:', error);
    return [];
  }
}

const fetchCatalogBrands = async () : Promise<Option[]> => {
  try {
    const response = await fetch('http://localhost:8080/product/brands');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching catalog brands:', error);
    return [];
  }
}

export default async function SidebarFilters() {
  const types = await fetchCatalogTypes();
  const brands = await fetchCatalogBrands();
  return (
    <div className="space-y-6 bg-white p-4 rounded-lg shadow">
      <FilterSection title="Brand" options={brands} />
      <FilterSection title="Type" options={types} />
    </div>
  );
}

function FilterSection({ title, options }: { title: string; options: Option[] }) {
  return (
    <div>
      <h4 className="font-semibold mb-2">{title}</h4>
      {options.map(opt => (
        <label key={opt.id} className="flex items-center space-x-2 mb-1">
          <input type="checkbox" className="form-checkbox" />
          <span className="text-gray-700">{opt.name}</span>
        </label>
      ))}
    </div>
  );
}