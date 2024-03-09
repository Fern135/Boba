// File: src/utils/utils.rs

pub struct Utils;

impl Utils {
    // Type checking functions
    pub fn is_string(value: &dyn ToString) -> bool {
        value.to_string().is_empty()
    }

    pub fn is_integer(value: &dyn ToString) -> bool {
        value.to_string().parse::<i64>().is_ok()
    }

    pub fn is_float(value: &dyn ToString) -> bool {
        value.to_string().parse::<f64>().is_ok()
    }

    pub fn is_boolean(value: &dyn ToString) -> bool {
        let lowercase_value = value.to_string().to_lowercase();
        lowercase_value == "true" || lowercase_value == "false"
    }

    pub fn is_array(value: &dyn ToString) -> bool {
        // Assuming arrays are represented as a string in this example
        value.to_string().starts_with("[") && value.to_string().ends_with("]")
    }

    // Type conversion functions
    pub fn to_string<T: ToString>(value: T) -> String {
        value.to_string()
    }

    pub fn to_int(value: &str) -> Option<i64> {
        value.parse().ok()
    }

    pub fn to_float(value: &str) -> Option<f64> {
        value.parse().ok()
    }

    pub fn to_bool(value: &str) -> Option<bool> {
        match value.to_lowercase().as_str() {
            "true" => Some(true),
            "false" => Some(false),
            _ => None,
        }
    }

    pub fn to_array(value: &str) -> Option<Vec<&str>> {
        // Assuming arrays are represented as a comma-separated string
        Some(value.split(',').map(str::trim).collect())
    }
}
