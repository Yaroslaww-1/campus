import qs from "qs";

export const stringifyParams = (params: unknown) =>
  qs.stringify(params, { arrayFormat: "comma", encodeValuesOnly: true, encode: false });

export const parseUrlParams = <T>(params: string): T => {
  const parsed = qs.parse(params, {
    comma: true,
    ignoreQueryPrefix: true,
    decoder(value) {
      if (/^(\d+|\d*\.\d+)$/.test(value)) {
        return parseFloat(value);
      }

      const keywords = {
        true: true,
        false: false,
        null: null,
        undefined: undefined,
      };
      
      if (value in keywords) {
        return keywords[value as keyof typeof keywords];
      }

      return value;
    },
  });
  return (parsed as unknown) as T;
};

export const updateQuerystringParams = (params: unknown) => {
  const newUrlParams = stringifyParams(params);
  window.history.replaceState(null, "", `?${newUrlParams}`);
};

export const updateQuerystringParam = (key: string, value: unknown) => {
  const oldParams = parseUrlParams<Record<string, unknown>>(window.location.search);
  const newUrlParams = stringifyParams({ ...oldParams, [key]: value });
  window.history.replaceState(null, "", `?${newUrlParams}`);
};