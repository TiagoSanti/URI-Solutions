SELECT d.name, v.name FROM products d JOIN providers v ON d.id_providers = v.id AND d.id_categories = 6;